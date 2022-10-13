all: clean collect process analyze

clean:
	rm -rf data

.PHONY: collect processed analysis
collect:
	# This target creates the data directory and adds the dataset from kaggle (https://www.kaggle.com/datasets/mrisdal/fake-news)
	mkdir data -p
	kaggle datasets download -d mrisdal/fake-news
	unzip fake-news.zip -d './data' 
	rm ./fake-news.zip

process:
	python3 src/data_cleaning/drop_columns.py				# Identify and Remove unnecessary columns
	python3 src/data_cleaning/replace_null_authors.py		# Replace 'null' authors with 'Anonymous'
	python3 src/data_cleaning/drop_na.py					# Remove rows with 'null' values
	python3 src/data_cleaning/drop_dup.py					# Remove duplicates from data
	python3 src/data_cleaning/date_format.py				# Format dates of 'published' column

analyze:
	# This target creates the plots directory with data analysis plots
	mkdir ./data/plots -p									# Create plots folder
	python3 src/data_analysis/data_quality.py				# Data Quality Plots (non-processed)
	python3 src/data_analysis/data_exploration.py			# Data Quality Plots (processed)
	python3 src/data_analysis/multiple_variables.py			# Relations Plots
