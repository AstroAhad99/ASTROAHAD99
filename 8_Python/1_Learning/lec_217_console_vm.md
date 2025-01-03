1. We can also run python on cmd.
2. We just need to type ```python``` on the cmd.
3. The following are the important commands that are used in cmd aka Command Prompt.
    - ```cd C:\Users\ahad9\Desktop``` to change the directory to another folder.
    - ```cd ..``` move one level up in the directory.
    - ```cd``` show current directory.
    - ```dir``` show the list of folders.
    - ```mkdir NewFolder``` make new folder.
    - ```rmdir NewFolder``` remove an empty directory.
    - ```rmdir /s Folder``` remove the directory having the content.
    - ```type nul example.txt``` to create an empty file.
    - ```copy example.txt D:\MyFolder``` copy the file to destination folder.
    - ```move example.txt new_example.txt``` rename files.
    - ```del example.txt``` to delete the files.
    - ```ipconfig``` to check the the ip configuration in the PC.
4. In python we can create virtual environment.
5. The following are the steps for creating virtual environment.
    - Check if the virtual environment library is intalled for not ```virtualenv --version```. If not then ```pip install virtualenv```.
    - Navigate to the directory.
    ```cd C:\Users\ahad9\Documents\ASTROAHAD99\8_Python\1_Learning\```.
    - Create a new virtual environment ```python -m venv myenv```
    - Activate the newly created virtual environment by ```myenv\Scripts\activate```
    - Run the file ```python lec_213_get_multi_pages.py```
    - If the libraries are missing then install those libraries.
    - This venv helps in doing testing.
    - To upgrade the pip then ```pip install --upgrade pip```
    - To check which libraries are installed in the venv then type ```pip freeze```.
    - Now to save the list of libraries that are installed into the venv then type ```pip freeze requirements.txt```
    - To install all the libraries in the requirements file then do ```pip install -r requirements.txt```
    - Finally deactivate the venv by ```myenv\Scripts\deactivate```
    - To remove the this folder type ```rmdir \s myenv```
6. Now we are going to create the virtual environment using pipenv
    - First install pipenv ```pip install pipenv```
    - Once the pipenv is installed then navigate to your directory ```cd C:\Users\ahad9\Documents\ASTROAHAD99\8_Python\1_Learning\```
    - Then install the virtual environment there ```pipenv install```
    - This will install virtual environment in another directory
    - Then type ```pipenv run python``` to run python
    - ```pipenv install <package name>``` to install library
    - ```pipenv run python lec_213_get_multi_pages.py``` to run the file
