---
title: projects_config
hide_title: false
hide_table_of_contents: false
keywords:
  - projects_config
  - ml
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
<tr><td><b>Name</b></td><td><code>projects_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.ml.projects_config</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `config` | `object` |  |
| `serviceAccount` | `string` | The service account Cloud ML uses to access resources in the project. |
| `serviceAccountProject` | `string` | The project number for `service_account`. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_getConfig` | `SELECT` | `projectsId` |
