---
title: status
hide_title: false
hide_table_of_contents: false
keywords:
  - status
  - contentwarehouse
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
<tr><td><b>Name</b></td><td><code>status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.contentwarehouse.status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `state` | `string` | State of the project. |
| `accessControlMode` | `string` | Access control mode. |
| `databaseType` | `string` | Database type. |
| `documentCreatorDefaultRole` | `string` | The default role for the person who create a document. |
| `location` | `string` | The location of the queried project. |
| `qaEnabled` | `boolean` | If the qa is enabled on this project. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_status` | `SELECT` | `locationsId, projectsId` |
