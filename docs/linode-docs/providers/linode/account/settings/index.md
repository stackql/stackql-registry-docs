---
title: settings
hide_title: false
hide_table_of_contents: false
keywords:
  - settings
  - account
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.account.settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `network_helper` | `boolean` | Enables network helper across all users by default for new Linodes and Linode Configs.<br /> |
| `object_storage` | `string` | A string describing the status of this account's Object Storage service enrollment.<br /> |
| `backups_enabled` | `boolean` | Account-wide backups default.  If `true`, all Linodes created will automatically be enrolled in the Backups service.  If `false`, Linodes will not be enrolled by default, but may still be enrolled on creation or later.<br /> |
| `longview_subscription` | `string` | The Longview Pro tier you are currently subscribed to. The value must be a [Longview Subscription](/docs/api/longview/#longview-subscriptions-list) ID or `null` for Longview Free.<br /> |
| `managed` | `boolean` | Our 24/7 incident response service. This robust, multi-homed monitoring system distributes monitoring checks to ensure that your servers remain online and available at all times. Linode Managed can monitor any service or software stack reachable over TCP or HTTP. Once you add a service to Linode Managed, we'll monitor it for connectivity, response, and total request time.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getAccountSettings` | `SELECT` |  | Returns information related to your Account settings: Managed service subscription, Longview subscription, and network helper.<br /> |
| `_getAccountSettings` | `EXEC` |  | Returns information related to your Account settings: Managed service subscription, Longview subscription, and network helper.<br /> |
| `enableAccountManaged` | `EXEC` |  | Enables Linode Managed for the entire account and sends a welcome email to the account's associated email address. Linode Managed can monitor any service or software stack reachable over TCP or HTTP. See our [Linode Managed guide](/docs/guides/linode-managed/) to learn more.<br /> |
| `updateAccountSettings` | `EXEC` |  | Updates your Account settings.<br /><br />To update your Longview subscription plan, send a request to [Update Longview Plan](/docs/api/longview/#longview-plan-update).<br /> |
