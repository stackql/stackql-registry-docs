---
title: companies
hide_title: false
hide_table_of_contents: false
keywords:
  - companies
  - jobs
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>companies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.jobs.companies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `companies` | `array` | Companies for the current client. |
| `metadata` | `object` | Additional information returned to client, such as debugging information. |
| `nextPageToken` | `string` | A token to retrieve the next page of results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `companiesId, projectsId, tenantsId` | Retrieves specified company. |
| `list` | `SELECT` | `projectsId, tenantsId` | Lists all companies associated with the project. |
| `create` | `INSERT` | `projectsId, tenantsId` | Creates a new company entity. |
| `delete` | `DELETE` | `companiesId, projectsId, tenantsId` | Deletes specified company. Prerequisite: The company has no jobs associated with it. |
| `patch` | `EXEC` | `companiesId, projectsId, tenantsId` | Updates specified company. |
