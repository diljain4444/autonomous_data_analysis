import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import PromptTemplate
from data_analysis_backend import workflow

st.title("AUTONOMOUS DATA ANALYSIS")

# ========== SIDEBAR ==========
st.sidebar.title("CHAT_BOT")
st.sidebar.button("NEW CHAT")

file = st.sidebar.file_uploader(
    "UPLOAD YOUR CSV HERE",
    type=["csv"]
)

if file is not None:
    st.sidebar.success("THE FILE IS UPLOADED")

    df = pd.read_csv(file)
    st.dataframe(df.head())

    columns_name = df.columns.tolist()

    user = st.chat_input("ENTER YOUR QUERY")

    # ========== PROMPT ==========
    prompt = PromptTemplate(
        template="""
You are a STRICT Python Data Analysis agent.

You MUST analyze an EXISTING pandas DataFrame named `df`.
The DataFrame `df` is already loaded from a user-uploaded CSV file.

ABSOLUTE RULES (VIOLATION = FAILURE):
- DO NOT import anything
- DO NOT create, overwrite, or redefine `df`
- DO NOT generate sample, random, or synthetic data
- DO NOT read or write files
- DO NOT use Streamlit
- DO NOT use plt.show()
- DO NOT create more than ONE plot
- DO NOT use df.plot.scatter on a Series
- Use scatter ONLY as: df.plot.scatter(x=..., y=...)

OUTPUT VARIABLE RULES:
- If the query produces a plot:
  assign it to variable named `fig`
- If the query produces tabular or numeric output:
  assign it to variable named `result`
- ALWAYS end the code by referencing the output variable (`fig` or `result`)

ALLOWED LIBRARIES (ALREADY AVAILABLE):
- pandas as pd
- numpy as np
- matplotlib.pyplot as plt

DATA CONSTRAINTS:
- DataFrame name: df
- Available columns: {columns_name}
- DO NOT assume any column outside this list
- If a referenced column does not exist:
  raise ValueError("Invalid column referenced in query")

ANALYSIS RULES:
- Statistics → pandas operations (mean, sum, count, median)
- Grouping → groupby
- Sorting → sort_values
- Filtering → boolean indexing
- Correlation → df.corr()
- Missing values → isnull(), dropna(), fillna()

PLOTTING RULES:
- ALWAYS start plotting with:
    fig, ax = plt.subplots()
- When using pandas plotting functions (e.g., df.plot.scatter, df.plot.bar):
    pass ax=ax to the plot function
- Do NOT assign df.plot(...) directly to fig
- Always set titles and axis labels for readability
- For subplots:
    use fig, axs = plt.subplots(...) and plot on each axs[i]
- ALWAYS return the Figure object as the last line: fig


- If a scatter plot is requested, use:
  fig, ax = plt.subplots()
  df.plot.scatter(x=..., y=..., ax=ax)
  ax.set_title(...)
  ax.set_xlabel(...)
  ax.set_ylabel(...)
  fig


OUTPUT FORMAT:
- Return ONLY valid executable Python code
- No markdown
- No comments
- No explanations
- No extra text
""",
        input_variables=["columns_name"]
    )

    final_system_prompt = prompt.format(columns_name=columns_name)




    # ========== RUN ==========
    if user:
        with st.chat_message("user"):
            st.markdown(user)
        output = workflow.invoke({
            "messages": [
                SystemMessage(content=final_system_prompt),
                HumanMessage(content=user)
            ]
        })

        raw_code = output["messages"][-1].content

# Remove markdown/code fences if present
        final_code = raw_code.strip()

        if final_code.startswith("```"):
          final_code = final_code.replace("```python", "")
          final_code = final_code.replace("```", "")
          final_code = final_code.strip()

        st.subheader("🧠 Generated Python Code")
        st.code(final_code, language="python")
        try:

          local_env = {
              "df": df,
              "pd": pd,
              "np": np,
              "plt": plt
          }

          exec(final_code, {}, local_env)

          # AFTER exec(final_code, globals(), local_env)

          if "fig" in local_env:
              st.pyplot(local_env["fig"])

          elif "result" in local_env:
              result = local_env["result"]

              if isinstance(result, pd.Series):
                  result = result.to_frame()

              if isinstance(result, pd.DataFrame):
                  if result.empty:
                      st.warning("⚠️ No data matched the given condition.")
                  else:
                      st.dataframe(result)
              else:
                  st.write(result)

          else:
              st.info("ℹ️ Analysis completed (no plot generated).")

        except Exception as e:

          st.error(f"❌ Execution Error: {e}")