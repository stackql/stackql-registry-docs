---
title: source_imports
hide_title: false
hide_table_of_contents: false
keywords:
  - source_imports
  - migrations
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>source_imports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.migrations.source_imports" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="authors_count" /> | `integer` |  |
| <CopyableCode code="authors_url" /> | `string` |  |
| <CopyableCode code="commit_count" /> | `integer` |  |
| <CopyableCode code="error_message" /> | `string` |  |
| <CopyableCode code="failed_step" /> | `string` |  |
| <CopyableCode code="has_large_files" /> | `boolean` |  |
| <CopyableCode code="html_url" /> | `string` |  |
| <CopyableCode code="import_percent" /> | `integer` |  |
| <CopyableCode code="large_files_count" /> | `integer` |  |
| <CopyableCode code="large_files_size" /> | `integer` |  |
| <CopyableCode code="message" /> | `string` |  |
| <CopyableCode code="project_choices" /> | `array` |  |
| <CopyableCode code="push_percent" /> | `integer` |  |
| <CopyableCode code="repository_url" /> | `string` |  |
| <CopyableCode code="status" /> | `string` |  |
| <CopyableCode code="status_text" /> | `string` |  |
| <CopyableCode code="svc_root" /> | `string` |  |
| <CopyableCode code="svn_root" /> | `string` |  |
| <CopyableCode code="tfvc_project" /> | `string` |  |
| <CopyableCode code="url" /> | `string` |  |
| <CopyableCode code="use_lfs" /> | `boolean` |  |
| <CopyableCode code="vcs" /> | `string` |  |
| <CopyableCode code="vcs_url" /> | `string` | The URL of the originating repository. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_import_status" /> | `SELECT` | <CopyableCode code="owner, repo" /> | View the progress of an import.<br /><br />**Warning:** Support for importing Mercurial, Subversion and Team Foundation Version Control repositories will end<br />on October 17, 2023. For more details, see [changelog](https://gh.io/github-importer-non-git-eol). In the coming weeks, we will update<br />these docs to reflect relevant changes to the API and will contact all integrators using the "Source imports" API.<br /><br />**Import status**<br /><br />This section includes details about the possible values of the `status` field of the Import Progress response.<br /><br />An import that does not have errors will progress through these steps:<br /><br />*   `detecting` - the "detection" step of the import is in progress because the request did not include a `vcs` parameter. The import is identifying the type of source control present at the URL.<br />*   `importing` - the "raw" step of the import is in progress. This is where commit data is fetched from the original repository. The import progress response will include `commit_count` (the total number of raw commits that will be imported) and `percent` (0 - 100, the current progress through the import).<br />*   `mapping` - the "rewrite" step of the import is in progress. This is where SVN branches are converted to Git branches, and where author updates are applied. The import progress response does not include progress information.<br />*   `pushing` - the "push" step of the import is in progress. This is where the importer updates the repository on GitHub. The import progress response will include `push_percent`, which is the percent value reported by `git push` when it is "Writing objects".<br />*   `complete` - the import is complete, and the repository is ready on GitHub.<br /><br />If there are problems, you will see one of these in the `status` field:<br /><br />*   `auth_failed` - the import requires authentication in order to connect to the original repository. To update authentication for the import, please see the [Update an import](https://docs.github.com/rest/migrations/source-imports#update-an-import) section.<br />*   `error` - the import encountered an error. The import progress response will include the `failed_step` and an error message. Contact [GitHub Support](https://support.github.com/contact?tags=dotcom-rest-api) for more information.<br />*   `detection_needs_auth` - the importer requires authentication for the originating repository to continue detection. To update authentication for the import, please see the [Update an import](https://docs.github.com/rest/migrations/source-imports#update-an-import) section.<br />*   `detection_found_nothing` - the importer didn't recognize any source control at the URL. To resolve, [Cancel the import](https://docs.github.com/rest/migrations/source-imports#cancel-an-import) and [retry](https://docs.github.com/rest/migrations/source-imports#start-an-import) with the correct URL.<br />*   `detection_found_multiple` - the importer found several projects or repositories at the provided URL. When this is the case, the Import Progress response will also include a `project_choices` field with the possible project choices as values. To update project choice, please see the [Update an import](https://docs.github.com/rest/migrations/source-imports#update-an-import) section.<br /><br />**The project_choices field**<br /><br />When multiple projects are found at the provided URL, the response hash will include a `project_choices` field, the value of which is an array of hashes each representing a project choice. The exact key/value pairs of the project hashes will differ depending on the version control type.<br /><br />**Git LFS related fields**<br /><br />This section includes details about Git LFS related fields that may be present in the Import Progress response.<br /><br />*   `use_lfs` - describes whether the import has been opted in or out of using Git LFS. The value can be `opt_in`, `opt_out`, or `undecided` if no action has been taken.<br />*   `has_large_files` - the boolean value describing whether files larger than 100MB were found during the `importing` step.<br />*   `large_files_size` - the total size in gigabytes of files larger than 100MB found in the originating repository.<br />*   `large_files_count` - the total number of files larger than 100MB found in the originating repository. To see a list of these files, make a "Get Large Files" request. |
| <CopyableCode code="cancel_import" /> | `EXEC` | <CopyableCode code="owner, repo" /> | Stop an import for a repository.<br /><br />**Warning:** Support for importing Mercurial, Subversion and Team Foundation Version Control repositories will end<br />on October 17, 2023. For more details, see [changelog](https://gh.io/github-importer-non-git-eol). In the coming weeks, we will update<br />these docs to reflect relevant changes to the API and will contact all integrators using the "Source imports" API.<br /> |
| <CopyableCode code="start_import" /> | `EXEC` | <CopyableCode code="owner, repo, data__vcs_url" /> | Start a source import to a GitHub repository using GitHub Importer. Importing into a GitHub repository with GitHub Actions enabled is not supported and will return a status `422 Unprocessable Entity` response.<br />**Warning:** Support for importing Mercurial, Subversion and Team Foundation Version Control repositories will end on October 17, 2023. For more details, see [changelog](https://gh.io/github-importer-non-git-eol). In the coming weeks, we will update these docs to reflect relevant changes to the API and will contact all integrators using the "Source imports" API. |
| <CopyableCode code="update_import" /> | `EXEC` | <CopyableCode code="owner, repo" /> | An import can be updated with credentials or a project choice by passing in the appropriate parameters in this API<br />request. If no parameters are provided, the import will be restarted.<br /><br />Some servers (e.g. TFS servers) can have several projects at a single URL. In those cases the import progress will<br />have the status `detection_found_multiple` and the Import Progress response will include a `project_choices` array.<br />You can select the project to import by providing one of the objects in the `project_choices` array in the update request.<br /><br />**Warning:** Support for importing Mercurial, Subversion and Team Foundation Version Control repositories will end<br />on October 17, 2023. For more details, see [changelog](https://gh.io/github-importer-non-git-eol). In the coming weeks, we will update<br />these docs to reflect relevant changes to the API and will contact all integrators using the "Source imports" API. |
