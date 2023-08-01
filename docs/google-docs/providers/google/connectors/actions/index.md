---
title: actions
hide_title: false
hide_table_of_contents: false
keywords:
  - actions
  - connectors
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
<tr><td><b>Name</b></td><td><code>actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.connectors.actions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Next page token if more actions available. |
| `unsupportedActionNames` | `array` | List of actions which contain unsupported Datatypes. Check datatype.proto for more information. |
| `actions` | `array` | List of action metadata. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `connectionsId, locationsId, projectsId` | Gets the schema of all the actions supported by the connector. |
| `execute` | `EXEC` | `actionsId, connectionsId, locationsId, projectsId` | Executes an action with the name specified in the request. The input parameters for executing the action are passed through the body of the ExecuteAction request. |
