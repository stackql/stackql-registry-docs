---
title: contents
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
<tr><td><b>Name</b></td><td><code>contents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.contents</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `name` | `string` |
| `target` | `string` |
| `git_url` | `string` |
| `sha` | `string` |
| `encoding` | `string` |
| `path` | `string` |
| `submodule_git_url` | `string` |
| `html_url` | `string` |
| `type` | `string` |
| `download_url` | `string` |
| `content` | `string` |
| `url` | `string` |
| `_links` | `object` |
| `size` | `integer` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_readme` | `SELECT` | `owner, repo` | Gets the preferred README for a repository.<br /><br />READMEs support [custom media types](https://docs.github.com/rest/reference/repos#custom-media-types) for retrieving the raw content or rendered HTML. |
| `get_readme_in_directory` | `SELECT` | `dir, owner, repo` | Gets the README from a repository directory.<br /><br />READMEs support [custom media types](https://docs.github.com/rest/reference/repos#custom-media-types) for retrieving the raw content or rendered HTML. |
| `create_or_update_file_contents` | `INSERT` | `owner, path, repo, data__content, data__message` | Creates a new file or replaces an existing file in a repository. |
| `delete_file` | `DELETE` | `owner, path, repo, data__message, data__sha` | Deletes a file in a repository.<br /><br />You can provide an additional `committer` parameter, which is an object containing information about the committer. Or, you can provide an `author` parameter, which is an object containing information about the author.<br /><br />The `author` section is optional and is filled in with the `committer` information if omitted. If the `committer` information is omitted, the authenticated user's information is used.<br /><br />You must provide values for both `name` and `email`, whether you choose to use `author` or `committer`. Otherwise, you'll receive a `422` status code. |
| `download_tarball_archive` | `EXEC` | `owner, ref, repo` | Gets a redirect URL to download a tar archive for a repository. If you omit `:ref`, the repository’s default branch (usually<br />`master`) will be used. Please make sure your HTTP framework is configured to follow redirects or you will need to use<br />the `Location` header to make a second `GET` request.<br />**Note**: For private repositories, these links are temporary and expire after five minutes. |
| `download_zipball_archive` | `EXEC` | `owner, ref, repo` | Gets a redirect URL to download a zip archive for a repository. If you omit `:ref`, the repository’s default branch (usually<br />`master`) will be used. Please make sure your HTTP framework is configured to follow redirects or you will need to use<br />the `Location` header to make a second `GET` request.<br />**Note**: For private repositories, these links are temporary and expire after five minutes. |
| `get_content` | `EXEC` | `owner, path, repo` | Gets the contents of a file or directory in a repository. Specify the file path or directory in `:path`. If you omit<br />`:path`, you will receive the contents of the repository's root directory. See the description below regarding what the API response includes for directories. <br /><br />Files and symlinks support [a custom media type](https://docs.github.com/rest/reference/repos#custom-media-types) for<br />retrieving the raw content or rendered HTML (when supported). All content types support [a custom media<br />type](https://docs.github.com/rest/reference/repos#custom-media-types) to ensure the content is returned in a consistent<br />object format.<br /><br />**Note**:<br />*   To get a repository's contents recursively, you can [recursively get the tree](https://docs.github.com/rest/reference/git#trees).<br />*   This API has an upper limit of 1,000 files for a directory. If you need to retrieve more files, use the [Git Trees<br />API](https://docs.github.com/rest/reference/git#get-a-tree).<br />*   This API supports files up to 1 megabyte in size.<br /><br />#### If the content is a directory<br />The response will be an array of objects, one object for each item in the directory.<br />When listing the contents of a directory, submodules have their "type" specified as "file". Logically, the value<br />_should_ be "submodule". This behavior exists in API v3 [for backwards compatibility purposes](https://git.io/v1YCW).<br />In the next major version of the API, the type will be returned as "submodule".<br /><br />#### If the content is a symlink <br />If the requested `:path` points to a symlink, and the symlink's target is a normal file in the repository, then the<br />API responds with the content of the file (in the format shown in the example. Otherwise, the API responds with an object <br />describing the symlink itself.<br /><br />#### If the content is a submodule<br />The `submodule_git_url` identifies the location of the submodule repository, and the `sha` identifies a specific<br />commit within the submodule repository. Git uses the given URL when cloning the submodule repository, and checks out<br />the submodule at that specific commit.<br /><br />If the submodule repository is not hosted on github.com, the Git URLs (`git_url` and `_links["git"]`) and the<br />github.com URLs (`html_url` and `_links["html"]`) will have null values. |
