---
title: mapping_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - mapping_rules
  - datamigration
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
<tr><td><b>Name</b></td><td><code>mapping_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datamigration.mapping_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `mappingRules` | `array` | The list of conversion workspace mapping rules. |
| `nextPageToken` | `string` | A token which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `conversionWorkspacesId, locationsId, mappingRulesId, projectsId` | Gets the details of a mapping rule. |
| `list` | `SELECT` | `conversionWorkspacesId, locationsId, projectsId` | Lists the mapping rules for a specific conversion workspace. |
| `create` | `INSERT` | `conversionWorkspacesId, locationsId, projectsId` | Creates a new mapping rule for a given conversion workspace. |
| `delete` | `DELETE` | `conversionWorkspacesId, locationsId, mappingRulesId, projectsId` | Deletes a single mapping rule. |
| `import` | `EXEC` | `conversionWorkspacesId, locationsId, projectsId` | Imports the mapping rules for a given conversion workspace. Supports various formats of external rules files. |
