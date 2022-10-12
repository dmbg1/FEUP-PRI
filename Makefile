# The all target helps automate the whole process: by running `make` from the command line, you can do everything in one go
# You can define further targets that only execute smaller subsets of your data pipeline according to your needs
all: clean collect process analyze

clean:
#	rm -rf data processed analysis

.PHONY: collect processed analysis adhoc
collect:
	# This target is usually associated with data collection
	# This can involved scraping websites, downloading files from servers,
	# or other similar operations.
	# As best practice, ensure that all output data goes to a known location (e.g., here, data/)
	kaggle datasets download -d mrisdal/fake-news
	unzip fake-news.zip -d './data' 
	rm ./fake-news.zip

process:
	# This target is reserved for data processing, which typically includes
	# cleaning and refinement.
	# As best practice, have multiple scripts to perform different (sub)steps
	# You may even opt for several targets for bigger granularity
	# (e.g., a process_cleaning and a process_refinement target)
	# Moreover, ensure that data also goes to a known location for easier analysis
	python3 src/data_cleaning/drop_columns.py						# Identify and Remove unnecessary columns
	python3 src/data_cleaning/replace_null_authors.py		# Replace 'null' authors with 'Anonymous'
	python3 src/data_cleaning/drop_na.py					# Remove rows with 'null' values
	python3 src/data_cleaning/drop_dup.py					# Remove duplicates from data
	python3 src/data_cleaning/date_format.py					# Format dates of 'published' column

analyze:
	# This target is recommended to isolate all data analysis scripts.
	# Once again, it is recommended to separate different types of analysis between scripts,
	# which may span several languages. Diversity is key here so data can be better understood.
	mkdir -p analysis/...
	Rscript code/produce_some_plots.R
	go run code/do_text_analysis.go

adhoc:
	# This target is not part of the overall automation, but it can be useful to have something similar
	# to automate some less frequent operation that you might want to run only when strictly necessary
	# (e.g., organize all produced data/analysis and run a notebook for an easier visual verification of obtained results)
	Rscript code/some_adhoc_script.R
