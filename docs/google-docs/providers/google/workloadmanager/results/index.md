---
title: results
hide_title: false
hide_table_of_contents: false
keywords:
  - results
  - workloadmanager
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
<tr><td><b>Name</b></td><td><code>results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.workloadmanager.results</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `documentationUrl` | `string` | the document url of the rule |
| `resource` | `object` | Message represent resource in execution result |
| `rule` | `string` | the rule which violate in execution |
| `severity` | `string` | severity of violation |
| `violationDetails` | `object` | Message describing the violdation in execution result |
| `violationMessage` | `string` | the violation message of an execution |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `evaluationsId, executionsId, locationsId, projectsId` |
| `_list` | `EXEC` | `evaluationsId, executionsId, locationsId, projectsId` |
