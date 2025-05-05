# autograde-viz

## Setup
`conda create --name <env_name> --file requirements.txt`
`conda activate <env_name>`

## Create package release
`python3 -m pip install build`

`python3 -m build --sdist`

`python3 -m build --wheel`


`twine check dist/*`

`twine upload dist/*` (or the newly built files in `dist/`)

username: `__token__`
password: api token
