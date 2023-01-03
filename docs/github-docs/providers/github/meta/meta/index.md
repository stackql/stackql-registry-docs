---
title: meta
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
<tr><td><b>Name</b></td><td><code>meta</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.meta.meta</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `ssh_keys` | `array` |
| `git` | `array` |
| `api` | `array` |
| `pages` | `array` |
| `verifiable_password_authentication` | `boolean` |
| `web` | `array` |
| `hooks` | `array` |
| `actions` | `array` |
| `packages` | `array` |
| `importer` | `array` |
| `dependabot` | `array` |
| `ssh_key_fingerprints` | `object` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` |  | Returns meta information about GitHub, including a list of GitHub's IP addresses. For more information, see "[About GitHub's IP addresses](https://docs.github.com/articles/about-github-s-ip-addresses/)."<br /><br />**Note:** The IP addresses shown in the documentation's response are only example values. You must always query the API directly to get the latest list of IP addresses. |
| `get_octocat` | `EXEC` |  | Get the octocat as ASCII art |
| `get_zen` | `EXEC` |  | Get a random sentence from the Zen of GitHub |
| `root` | `EXEC` |  | Get Hypermedia links to resources accessible in GitHub's REST API |
