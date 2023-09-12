---
title: orgs
hide_title: false
hide_table_of_contents: false
keywords:
  - orgs
  - codespaces
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
<tr><td><b>Name</b></td><td><code>orgs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.codespaces.orgs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `codespaces` | `array` |
| `total_count` | `integer` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_in_organization` | `SELECT` | `org` | Lists the codespaces associated to a specified organization.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `set_codespaces_access` | `EXEC` | `org, data__visibility` | Sets which users can access codespaces in an organization. This is synonymous with granting or revoking codespaces access permissions for users according to the visibility.<br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
