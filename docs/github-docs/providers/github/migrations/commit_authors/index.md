---
title: commit_authors
hide_title: false
hide_table_of_contents: false
keywords:
  - commit_authors
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>commit_authors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.migrations.commit_authors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `remote_name` | `string` |
| `url` | `string` |
| `email` | `string` |
| `import_url` | `string` |
| `remote_id` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_commit_authors` | `SELECT` | `owner, repo` | Each type of source control system represents authors in a different way. For example, a Git commit author has a display name and an email address, but a Subversion commit author just has a username. The GitHub Importer will make the author information valid, but the author might not be correct. For example, it will change the bare Subversion username `hubot` into something like `hubot &lt;hubot@12341234-abab-fefe-8787-fedcba987654&gt;`.<br /><br />This endpoint and the [Map a commit author](https://docs.github.com/rest/migrations/source-imports#map-a-commit-author) endpoint allow you to provide correct Git author information.<br /><br />**Warning:** Support for importing Mercurial, Subversion and Team Foundation Version Control repositories will end<br />on October 17, 2023. For more details, see [changelog](https://gh.io/github-importer-non-git-eol). In the coming weeks, we will update<br />these docs to reflect relevant changes to the API and will contact all integrators using the "Source imports" API. |
| `map_commit_author` | `EXEC` | `author_id, owner, repo` | Update an author's identity for the import. Your application can continue updating authors any time before you push<br />new commits to the repository.<br /><br />**Warning:** Support for importing Mercurial, Subversion and Team Foundation Version Control repositories will end<br />on October 17, 2023. For more details, see [changelog](https://gh.io/github-importer-non-git-eol). In the coming weeks, we will update<br />these docs to reflect relevant changes to the API and will contact all integrators using the "Source imports" API.<br /> |
