---
title: source_imports
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>source_imports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.migrations.source_imports</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tfvc_project` | `string` |  |
| `large_files_count` | `integer` |  |
| `error_message` | `string` |  |
| `failed_step` | `string` |  |
| `use_lfs` | `boolean` |  |
| `authors_count` | `integer` |  |
| `authors_url` | `string` |  |
| `status` | `string` |  |
| `repository_url` | `string` |  |
| `url` | `string` |  |
| `push_percent` | `integer` |  |
| `commit_count` | `integer` |  |
| `large_files_size` | `integer` |  |
| `svn_root` | `string` |  |
| `vcs_url` | `string` | The URL of the originating repository. |
| `project_choices` | `array` |  |
| `message` | `string` |  |
| `svc_root` | `string` |  |
| `html_url` | `string` |  |
| `status_text` | `string` |  |
| `import_percent` | `integer` |  |
| `vcs` | `string` |  |
| `has_large_files` | `boolean` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_import_status` | `SELECT` | `owner, repo` | View the progress of an import.<br /><br />**Import status**<br /><br />This section includes details about the possible values of the `status` field of the Import Progress response.<br /><br />An import that does not have errors will progress through these steps:<br /><br />*   `detecting` - the "detection" step of the import is in progress because the request did not include a `vcs` parameter. The import is identifying the type of source control present at the URL.<br />*   `importing` - the "raw" step of the import is in progress. This is where commit data is fetched from the original repository. The import progress response will include `commit_count` (the total number of raw commits that will be imported) and `percent` (0 - 100, the current progress through the import).<br />*   `mapping` - the "rewrite" step of the import is in progress. This is where SVN branches are converted to Git branches, and where author updates are applied. The import progress response does not include progress information.<br />*   `pushing` - the "push" step of the import is in progress. This is where the importer updates the repository on GitHub. The import progress response will include `push_percent`, which is the percent value reported by `git push` when it is "Writing objects".<br />*   `complete` - the import is complete, and the repository is ready on GitHub.<br /><br />If there are problems, you will see one of these in the `status` field:<br /><br />*   `auth_failed` - the import requires authentication in order to connect to the original repository. To update authentication for the import, please see the [Update an import](https://docs.github.com/rest/reference/migrations#update-an-import) section.<br />*   `error` - the import encountered an error. The import progress response will include the `failed_step` and an error message. Contact [GitHub Support](https://support.github.com/contact?tags=dotcom-rest-api) for more information.<br />*   `detection_needs_auth` - the importer requires authentication for the originating repository to continue detection. To update authentication for the import, please see the [Update an import](https://docs.github.com/rest/reference/migrations#update-an-import) section.<br />*   `detection_found_nothing` - the importer didn't recognize any source control at the URL. To resolve, [Cancel the import](https://docs.github.com/rest/reference/migrations#cancel-an-import) and [retry](https://docs.github.com/rest/reference/migrations#start-an-import) with the correct URL.<br />*   `detection_found_multiple` - the importer found several projects or repositories at the provided URL. When this is the case, the Import Progress response will also include a `project_choices` field with the possible project choices as values. To update project choice, please see the [Update an import](https://docs.github.com/rest/reference/migrations#update-an-import) section.<br /><br />**The project_choices field**<br /><br />When multiple projects are found at the provided URL, the response hash will include a `project_choices` field, the value of which is an array of hashes each representing a project choice. The exact key/value pairs of the project hashes will differ depending on the version control type.<br /><br />**Git LFS related fields**<br /><br />This section includes details about Git LFS related fields that may be present in the Import Progress response.<br /><br />*   `use_lfs` - describes whether the import has been opted in or out of using Git LFS. The value can be `opt_in`, `opt_out`, or `undecided` if no action has been taken.<br />*   `has_large_files` - the boolean value describing whether files larger than 100MB were found during the `importing` step.<br />*   `large_files_size` - the total size in gigabytes of files larger than 100MB found in the originating repository.<br />*   `large_files_count` - the total number of files larger than 100MB found in the originating repository. To see a list of these files, make a "Get Large Files" request. |
| `cancel_import` | `EXEC` | `owner, repo` | Stop an import for a repository. |
| `start_import` | `EXEC` | `owner, repo, data__vcs_url` | Start a source import to a GitHub repository using GitHub Importer. |
| `update_import` | `EXEC` | `owner, repo` | An import can be updated with credentials or a project choice by passing in the appropriate parameters in this API<br />request. If no parameters are provided, the import will be restarted. |
