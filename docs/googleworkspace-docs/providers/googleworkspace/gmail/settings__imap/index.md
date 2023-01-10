---
title: settings__imap
hide_title: false
hide_table_of_contents: false
keywords:
  - settings__imap
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
<tr><td><b>Name</b></td><td><code>settings__imap</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.gmail.settings__imap</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `enabled` | `boolean` | Whether IMAP is enabled for the account. |
| `expungeBehavior` | `string` | The action that will be executed on a message when it is marked as deleted and expunged from the last visible IMAP folder. |
| `maxFolderSize` | `integer` | An optional limit on the number of messages that an IMAP folder may contain. Legal values are 0, 1000, 2000, 5000 or 10000. A value of zero is interpreted to mean that there is no limit. |
| `autoExpunge` | `boolean` | If this value is true, Gmail will immediately expunge a message when it is marked as deleted in IMAP. Otherwise, Gmail will wait for an update from the client before expunging messages marked as deleted. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `users_settings_getImap` | `SELECT` | `userId` |
