---
title: settings__pop
hide_title: false
hide_table_of_contents: false
keywords:
  - settings__pop
  - gmail
  - googleworkspace    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleworkspace/stackql-googleworkspace-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>settings__pop</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.gmail.settings__pop</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `accessWindow` | `string` | The range of messages which are accessible via POP. |
| `disposition` | `string` | The action that will be executed on a message after it has been fetched via POP. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `users_settings_getPop` | `SELECT` | `userId` |
