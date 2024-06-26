---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - databases
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
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.databases.instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | A unique ID that can be used to identify and reference the Managed Database. |
| <CopyableCode code="allow_list" /> | `array` | A list of IP addresses that can access the Managed Database. Each item can be a single IP address or a range in CIDR format.<br /><br />By default, this is an empty array (`[]`), which blocks all connections (both public and private) to the Managed Database.<br /><br />If `0.0.0.0/0` is a value in this list, then all IP addresses can access the Managed Database.<br /> |
| <CopyableCode code="cluster_size" /> | `integer` | The number of Linode Instance nodes deployed to the Managed Database.<br /><br />Choosing 3 nodes creates a high availability cluster consisting of 1 primary node and 2 replica nodes.<br /> |
| <CopyableCode code="created" /> | `string` | When this Managed Database was created. |
| <CopyableCode code="encrypted" /> | `boolean` | Whether the Managed Databases is encrypted. |
| <CopyableCode code="engine" /> | `string` | The Managed Database engine type. |
| <CopyableCode code="hosts" /> | `object` | The primary and secondary hosts for the Managed Database. These are assigned after provisioning is complete. |
| <CopyableCode code="instance_uri" /> | `string` | Append this to `https://api.linode.com` to run commands for the Managed Database.<br /> |
| <CopyableCode code="label" /> | `string` | A unique, user-defined string referring to the Managed Database. |
| <CopyableCode code="region" /> | `string` | The [Region](/docs/api/regions/) ID for the Managed Database. |
| <CopyableCode code="status" /> | `string` | The operating status of the Managed Database. |
| <CopyableCode code="type" /> | `string` | The Linode Instance type used by the Managed Database for its nodes. |
| <CopyableCode code="updated" /> | `string` | When this Managed Database was last updated. |
| <CopyableCode code="updates" /> | `object` | Configuration settings for automated patch update maintenance for the Managed Database. |
| <CopyableCode code="version" /> | `string` | The Managed Database engine version. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="getDatabasesInstances" /> | `SELECT` |  |
| <CopyableCode code="_getDatabasesInstances" /> | `EXEC` |  |
