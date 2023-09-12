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
| `download_url` | `string` |
| `content-submodule__links` | `object` |
| `sha` | `string` |
| `content-submodule_name` | `string` |
| `type` | `string` |
| `submodule_git_url` | `string` |
| `content-submodule_download_url` | `string` |
| `content-submodule_git_url` | `string` |
| `content-symlink_target` | `string` |
| `content-symlink_path` | `string` |
| `content-symlink_download_url` | `string` |
| `_links` | `object` |
| `content-submodule_submodule_git_url` | `string` |
| `content-symlink_name` | `string` |
| `content-symlink_size` | `integer` |
| `content-symlink_sha` | `string` |
| `content-symlink_html_url` | `string` |
| `content-symlink_git_url` | `string` |
| `git_url` | `string` |
| `content-submodule_url` | `string` |
| `content-submodule_size` | `integer` |
| `url` | `string` |
| `encoding` | `string` |
| `content-submodule_path` | `string` |
| `content-submodule_html_url` | `string` |
| `target` | `string` |
| `content` | `string` |
| `content-symlink_url` | `string` |
| `content-submodule_type` | `string` |
| `content-symlink__links` | `object` |
| `size` | `integer` |
| `content-submodule_sha` | `string` |
| `path` | `string` |
| `content-symlink_type` | `string` |
| `html_url` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_content` | `SELECT` | `owner, path, repo` | Gets the contents of a file or directory in a repository. Specify the file path or directory in `:path`. If you omit<br />`:path`, you will receive the contents of the repository's root directory. See the description below regarding what the API response includes for directories. <br /><br />Files and symlinks support [a custom media type](https://docs.github.com/rest/overview/media-types) for<br />retrieving the raw content or rendered HTML (when supported). All content types support [a custom media<br />type](https://docs.github.com/rest/overview/media-types) to ensure the content is returned in a consistent<br />object format.<br /><br />**Notes**:<br />*   To get a repository's contents recursively, you can [recursively get the tree](https://docs.github.com/rest/git/trees#get-a-tree).<br />*   This API has an upper limit of 1,000 files for a directory. If you need to retrieve more files, use the [Git Trees<br />API](https://docs.github.com/rest/git/trees#get-a-tree).<br /> *  Download URLs expire and are meant to be used just once. To ensure the download URL does not expire, please use the contents API to obtain a fresh download URL for each download.<br /> Size limits:<br />If the requested file's size is:<br />* 1 MB or smaller: All features of this endpoint are supported.<br />* Between 1-100 MB: Only the `raw` or `object` [custom media types](https://docs.github.com/rest/repos/contents#custom-media-types-for-repository-contents) are supported. Both will work as normal, except that when using the `object` media type, the `content` field will be an empty string and the `encoding` field will be `"none"`. To get the contents of these larger files, use the `raw` media type.<br /> * Greater than 100 MB: This endpoint is not supported.<br /><br /> If the content is a directory:<br />The response will be an array of objects, one object for each item in the directory.<br />When listing the contents of a directory, submodules have their "type" specified as "file". Logically, the value<br />_should_ be "submodule". This behavior exists in API v3 [for backwards compatibility purposes](https://git.io/v1YCW).<br />In the next major version of the API, the type will be returned as "submodule".<br /><br /> If the content is a symlink: <br />If the requested `:path` points to a symlink, and the symlink's target is a normal file in the repository, then the<br />API responds with the content of the file (in the format shown in the example. Otherwise, the API responds with an object <br />describing the symlink itself.<br /><br /> If the content is a submodule:<br />The `submodule_git_url` identifies the location of the submodule repository, and the `sha` identifies a specific<br />commit within the submodule repository. Git uses the given URL when cloning the submodule repository, and checks out<br />the submodule at that specific commit.<br /><br />If the submodule repository is not hosted on github.com, the Git URLs (`git_url` and `_links["git"]`) and the<br />github.com URLs (`html_url` and `_links["html"]`) will have null values. |
| `delete_file` | `DELETE` | `owner, path, repo, data__message, data__sha` | Deletes a file in a repository.<br /><br />You can provide an additional `committer` parameter, which is an object containing information about the committer. Or, you can provide an `author` parameter, which is an object containing information about the author.<br /><br />The `author` section is optional and is filled in with the `committer` information if omitted. If the `committer` information is omitted, the authenticated user's information is used.<br /><br />You must provide values for both `name` and `email`, whether you choose to use `author` or `committer`. Otherwise, you'll receive a `422` status code.<br /><br />**Note:** If you use this endpoint and the "[Create or update file contents](https://docs.github.com/rest/repos/contents/#create-or-update-file-contents)" endpoint in parallel, the concurrent requests will conflict and you will receive errors. You must use these endpoints serially instead. |
| `create_or_update_file_contents` | `EXEC` | `owner, path, repo, data__content, data__message` | Creates a new file or replaces an existing file in a repository. You must authenticate using an access token with the `repo` scope to use this endpoint. If you want to modify files in the `.github/workflows` directory, you must authenticate using an access token with the `workflow` scope.<br /><br />**Note:** If you use this endpoint and the "[Delete a file](https://docs.github.com/rest/repos/contents/#delete-a-file)" endpoint in parallel, the concurrent requests will conflict and you will receive errors. You must use these endpoints serially instead. |
