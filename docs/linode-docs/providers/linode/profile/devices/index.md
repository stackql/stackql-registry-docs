---
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
  - profile
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
<tr><td><b>Name</b></td><td><code>devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.profile.devices" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | The unique ID for this TrustedDevice |
| <CopyableCode code="created" /> | `string` | When this Remember Me session was started.  This corresponds to the time of login with the "Remember Me" box checked.<br /> |
| <CopyableCode code="expiry" /> | `string` | When this TrustedDevice session expires.  Sessions typically last 30 days.<br /> |
| <CopyableCode code="last_authenticated" /> | `string` | The last time this TrustedDevice was successfully used to authenticate to &lt;a target="_top" href="https://login.linode.com"&gt;login.linode.com&lt;/a&gt;.<br /> |
| <CopyableCode code="last_remote_addr" /> | `string` | The last IP Address to successfully authenticate with this TrustedDevice.<br /> |
| <CopyableCode code="user_agent" /> | `string` | The User Agent of the browser that created this TrustedDevice session.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getDevices" /> | `SELECT` |  | Returns a paginated list of active TrustedDevices for your User. Browsers with an active Remember Me Session are logged into your account until the session expires or is revoked.<br /> |
| <CopyableCode code="getTrustedDevice" /> | `SELECT` | <CopyableCode code="deviceId" /> | Returns a single active TrustedDevice for your User.<br /> |
| <CopyableCode code="_getDevices" /> | `EXEC` |  | Returns a paginated list of active TrustedDevices for your User. Browsers with an active Remember Me Session are logged into your account until the session expires or is revoked.<br /> |
| <CopyableCode code="_getTrustedDevice" /> | `EXEC` | <CopyableCode code="deviceId" /> | Returns a single active TrustedDevice for your User.<br /> |
| <CopyableCode code="revokeTrustedDevice" /> | `EXEC` | <CopyableCode code="deviceId" /> | Revoke an active TrustedDevice for your User.  Once a TrustedDevice is revoked, this device will have to log in again before accessing your Linode account.<br /> |
