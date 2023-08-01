---
title: ssh_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - ssh_keys
  - baremetalsolution
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
<tr><td><b>Name</b></td><td><code>ssh_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.baremetalsolution.ssh_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
| `sshKeys` | `array` | The SSH keys registered in the project. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `locationsId, projectsId` | Lists the public SSH keys registered for the specified project. These SSH keys are used only for the interactive serial console feature. |
| `create` | `INSERT` | `locationsId, projectsId` | Register a public SSH key in the specified project for use with the interactive serial console feature. |
| `delete` | `DELETE` | `locationsId, projectsId, sshKeysId` | Deletes a public SSH key registered in the specified project. |
