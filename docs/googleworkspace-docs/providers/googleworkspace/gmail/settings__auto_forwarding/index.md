---
title: settings__auto_forwarding
hide_title: false
hide_table_of_contents: false
keywords:
  - settings__auto_forwarding
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
<tr><td><b>Name</b></td><td><code>settings__auto_forwarding</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.gmail.settings__auto_forwarding</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `emailAddress` | `string` | Email address to which all incoming messages are forwarded. This email address must be a verified member of the forwarding addresses. |
| `enabled` | `boolean` | Whether all incoming mail is automatically forwarded to another address. |
| `disposition` | `string` | The state that a message should be left in after it has been forwarded. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `users_settings_getAutoForwarding` | `SELECT` | `userId` |
