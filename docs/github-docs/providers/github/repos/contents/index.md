---
title: contents
hide_title: false
hide_table_of_contents: false
keywords:
  - contents
  - repos
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>contents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.contents</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `name` | `string` |
| `sha` | `string` |
| `size` | `integer` |
| `encoding` | `string` |
| `path` | `string` |
| `_links` | `object` |
| `content` | `string` |
| `target` | `string` |
| `type` | `string` |
| `url` | `string` |
| `git_url` | `string` |
| `download_url` | `string` |
| `submodule_git_url` | `string` |
| `html_url` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_readme` | `SELECT` | `owner, repo` | Gets the preferred README for a repository.<br /><br />READMEs support [custom media types](https://docs.github.com/rest/overview/media-types) for retrieving the raw content or rendered HTML. |
| `get_readme_in_directory` | `SELECT` | `dir, owner, repo` | Gets the README from a repository directory.<br /><br />READMEs support [custom media types](https://docs.github.com/rest/overview/media-types) for retrieving the raw content or rendered HTML. |
| `delete_file` | `DELETE` | `owner, path, repo, data__message, data__sha` | Deletes a file in a repository.<br /><br />You can provide an additional `committer` parameter, which is an object containing information about the committer. Or, you can provide an `author` parameter, which is an object containing information about the author.<br /><br />The `author` section is optional and is filled in with the `committer` information if omitted. If the `committer` information is omitted, the authenticated user's information is used.<br /><br />You must provide values for both `name` and `email`, whether you choose to use `author` or `committer`. Otherwise, you'll receive a `422` status code.<br /><br />**Note:** If you use this endpoint and the "[Create or update file contents](https://docs.github.com/rest/repos/contents/#create-or-update-file-contents)" endpoint in parallel, the concurrent requests will conflict and you will receive errors. You must use these endpoints serially instead. |
| `create_or_update_file_contents` | `EXEC` | `owner, path, repo, data__content, data__message` | Creates a new file or replaces an existing file in a repository. You must authenticate using an access token with the `repo` scope to use this endpoint. If you want to modify files in the `.github/workflows` directory, you must authenticate using an access token with the `workflow` scope.<br /><br />**Note:** If you use this endpoint and the "[Delete a file](https://docs.github.com/rest/repos/contents/#delete-a-file)" endpoint in parallel, the concurrent requests will conflict and you will receive errors. You must use these endpoints serially instead. |
| `download_tarball_archive` | `EXEC` | `owner, ref, repo` | Gets a redirect URL to download a tar archive for a repository. If you omit `:ref`, the repository’s default branch (usually<br />`main`) will be used. Please make sure your HTTP framework is configured to follow redirects or you will need to use<br />the `Location` header to make a second `GET` request.<br />**Note**: For private repositories, these links are temporary and expire after five minutes. |
| `download_zipball_archive` | `EXEC` | `owner, ref, repo` | Gets a redirect URL to download a zip archive for a repository. If you omit `:ref`, the repository’s default branch (usually<br />`main`) will be used. Please make sure your HTTP framework is configured to follow redirects or you will need to use<br />the `Location` header to make a second `GET` request.<br /><br />**Note**: For private repositories, these links are temporary and expire after five minutes. If the repository is empty, you will receive a 404 when you follow the redirect. |
