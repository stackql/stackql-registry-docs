---
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - rules
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
<tr><td><b>Name</b></td><td><code>rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.workloadmanager.rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | rule name |
| `description` | `string` | descrite rule in plain language |
| `remediation` | `string` | the remediation for the rule |
| `displayName` | `string` | the name display in UI |
| `secondaryCategory` | `string` | the secondary category |
| `revisionId` | `string` | Output only. the version of the rule |
| `uri` | `string` | the docuement url for the rule |
| `primaryCategory` | `string` | the primary category |
| `severity` | `string` | the severity of the rule |
| `errorMessage` | `string` | the message template for rule |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `locationsId, projectsId` |
| `_list` | `EXEC` | `locationsId, projectsId` |
