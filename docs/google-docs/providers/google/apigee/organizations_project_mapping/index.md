---
title: organizations_project_mapping
hide_title: false
hide_table_of_contents: false
keywords:
  - organizations_project_mapping
  - apigee
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
<tr><td><b>Name</b></td><td><code>organizations_project_mapping</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.organizations_project_mapping</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `projectId` | `string` | Google Cloud project associated with the Apigee organization |
| `projectIds` | `array` | DEPRECATED: Use `project_id`. An Apigee Organization is mapped to a single project. |
| `location` | `string` | Output only. The Google Cloud region where control plane data is located. For more information, see https://cloud.google.com/about/locations/. |
| `organization` | `string` | Name of the Apigee organization. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `organizations_getProjectMapping` | `SELECT` | `organizationsId` |
