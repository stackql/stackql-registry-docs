---
title: iot_hubs
hide_title: false
hide_table_of_contents: false
keywords:
  - iot_hubs
  - iot_hub
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>iot_hubs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>iot_hubs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_hub.iot_hubs" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="manual_failover" /> | `EXEC` | <CopyableCode code="iotHubName, resourceGroupName, subscriptionId, data__failoverRegion" /> | Manually initiate a failover for the IoT Hub to its secondary region. To learn more, see https://aka.ms/manualfailover |
