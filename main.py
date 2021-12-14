from src.DataAnalysisSystem import DataAnalysisSystem

if __name__ == "__main__":

    data_dir_path = "data"

    das = DataAnalysisSystem(data_dir_path)

    das.run_analysis_full()
