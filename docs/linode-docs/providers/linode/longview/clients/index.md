---
title: clients
hide_title: false
hide_table_of_contents: false
keywords:
  - clients
  - longview
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clients</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.longview.clients" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | This Client's unique ID.<br /> |
| <CopyableCode code="api_key" /> | `string` | The API key for this Client, used when configuring the Longview<br />Client application on your Linode.<br /><br />Returns as `[REDACTED]` if you do not have read-write access to this client.<br /> |
| <CopyableCode code="apps" /> | `object` | The apps this Client is monitoring on your Linode. This is configured when you install the Longview Client application, and is present here for information purposes only.<br /> |
| <CopyableCode code="created" /> | `string` | When this Longview Client was created.<br /> |
| <CopyableCode code="install_code" /> | `string` | The install code for this Client, used when configuring the Longview<br />Client application on your Linode.<br /><br />Returns as `[REDACTED]` if you do not have read-write access to this client.<br /> |
| <CopyableCode code="label" /> | `string` | This Client's unique label. This is for display purposes only.<br /> |
| <CopyableCode code="updated" /> | `string` | When this Longview Client was last updated.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getLongviewClient" /> | `SELECT` | <CopyableCode code="clientId" /> | Returns a single Longview Client you can access.<br /> |
| <CopyableCode code="getLongviewClients" /> | `SELECT` |  | Returns a paginated list of Longview Clients you have access to. Longview Client is used to monitor stats on your Linode with the help of the Longview Client application.<br /> |
| <CopyableCode code="createLongviewClient" /> | `INSERT` |  | Creates a Longview Client.  This Client will not begin monitoring the status of your server until you configure the Longview Client application on your Linode using the returning `install_code` and `api_key`.<br /> |
| <CopyableCode code="deleteLongviewClient" /> | `DELETE` | <CopyableCode code="clientId" /> | Deletes a Longview Client from your Account.<br /><br />**All information stored for this client will be lost.**<br /><br />This _does not_ uninstall the Longview Client application for your Linode - you must do that manually.<br /> |
| <CopyableCode code="_getLongviewClient" /> | `EXEC` | <CopyableCode code="clientId" /> | Returns a single Longview Client you can access.<br /> |
| <CopyableCode code="_getLongviewClients" /> | `EXEC` |  | Returns a paginated list of Longview Clients you have access to. Longview Client is used to monitor stats on your Linode with the help of the Longview Client application.<br /> |
| <CopyableCode code="updateLongviewClient" /> | `EXEC` | <CopyableCode code="clientId" /> | Updates a Longview Client.  This cannot update how it monitors your server; use the Longview Client application on your Linode for monitoring configuration.<br /> |
