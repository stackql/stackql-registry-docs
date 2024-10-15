---
title: device_capacity_checks
hide_title: false
hide_table_of_contents: false
keywords:
  - device_capacity_checks
  - data_box_edge
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

Creates, updates, deletes, gets or lists a <code>device_capacity_checks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>device_capacity_checks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_box_edge.device_capacity_checks" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="check_resource_creation_feasibility" /> | `EXEC` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId, data__properties" /> | Posts the device capacity request info to check feasibility. |
