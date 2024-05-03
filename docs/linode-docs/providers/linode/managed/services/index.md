---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - managed
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.managed.services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | This Service's unique ID.<br /> |
| <CopyableCode code="address" /> | `string` | The URL at which this Service is monitored.<br /><br />URL parameters such as `?no-cache=1` are preserved.<br /><br />URL fragments/anchors such as `#monitor` are **not** preserved.<br /> |
| <CopyableCode code="body" /> | `string` | What to expect to find in the response body for the Service to be considered up.<br /> |
| <CopyableCode code="consultation_group" /> | `string` | The group of ManagedContacts who should be notified or consulted with when an Issue is detected.<br /> |
| <CopyableCode code="created" /> | `string` | When this Managed Service was created. |
| <CopyableCode code="credentials" /> | `array` | An array of ManagedCredential IDs that should be used when attempting to resolve issues with this Service.<br /> |
| <CopyableCode code="label" /> | `string` | The label for this Service. This is for display purposes only.<br /> |
| <CopyableCode code="notes" /> | `string` | Any information relevant to the Service that Linode special forces should know when attempting to resolve Issues.<br /> |
| <CopyableCode code="region" /> | `string` | The Region in which this Service is located. This is required if address is a private IP, and may not be set otherwise.<br /> |
| <CopyableCode code="service_type" /> | `string` | How this Service is monitored.<br /> |
| <CopyableCode code="status" /> | `string` | The current status of this Service.<br /> |
| <CopyableCode code="timeout" /> | `integer` | How long to wait, in seconds, for a response before considering the Service to be down.<br /> |
| <CopyableCode code="updated" /> | `string` | When this Managed Service was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getManagedService" /> | `SELECT` | <CopyableCode code="serviceId" /> | Returns information about a single Managed Service on your Account.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| <CopyableCode code="getManagedServices" /> | `SELECT` |  | Returns a paginated list of Managed Services on your Account. These<br />are the services Linode Managed is monitoring and will report and attempt<br />to resolve issues with.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| <CopyableCode code="createManagedService" /> | `INSERT` | <CopyableCode code="data__address, data__label, data__service_type, data__timeout" /> | Creates a Managed Service. Linode Managed will begin monitoring this<br />service and reporting and attempting to resolve any Issues.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| <CopyableCode code="deleteManagedService" /> | `DELETE` | <CopyableCode code="serviceId" /> | Deletes a Managed Service.  This service will no longer be monitored by<br />Linode Managed.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| <CopyableCode code="_getManagedService" /> | `EXEC` | <CopyableCode code="serviceId" /> | Returns information about a single Managed Service on your Account.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| <CopyableCode code="_getManagedServices" /> | `EXEC` |  | Returns a paginated list of Managed Services on your Account. These<br />are the services Linode Managed is monitoring and will report and attempt<br />to resolve issues with.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| <CopyableCode code="disableManagedService" /> | `EXEC` | <CopyableCode code="serviceId" /> | Temporarily disables monitoring of a Managed Service.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| <CopyableCode code="enableManagedService" /> | `EXEC` | <CopyableCode code="serviceId" /> | Enables monitoring of a Managed Service.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| <CopyableCode code="updateManagedService" /> | `EXEC` | <CopyableCode code="serviceId" /> | Updates information about a Managed Service.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
