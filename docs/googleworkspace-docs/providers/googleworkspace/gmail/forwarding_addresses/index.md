---
title: forwarding_addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - forwarding_addresses
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
<tr><td><b>Name</b></td><td><code>forwarding_addresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.gmail.forwarding_addresses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `forwardingEmail` | `string` | An email address to which messages can be forwarded. |
| `verificationStatus` | `string` | Indicates whether this address has been verified and is usable for forwarding. Read-only. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `users_settings_forwardingAddresses_get` | `SELECT` | `forwardingEmail, userId` | Gets the specified forwarding address. |
| `users_settings_forwardingAddresses_list` | `SELECT` | `userId` | Lists the forwarding addresses for the specified account. |
| `users_settings_forwardingAddresses_create` | `INSERT` | `userId` | Creates a forwarding address. If ownership verification is required, a message will be sent to the recipient and the resource's verification status will be set to `pending`; otherwise, the resource will be created with verification status set to `accepted`. This method is only available to service account clients that have been delegated domain-wide authority. |
| `users_settings_forwardingAddresses_delete` | `DELETE` | `forwardingEmail, userId` | Deletes the specified forwarding address and revokes any verification that may have been required. This method is only available to service account clients that have been delegated domain-wide authority. |
