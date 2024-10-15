---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - app_service
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

Creates, updates, deletes, gets or lists a <code>operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.operations" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="subscriptionId, data__name, data__type" /> | Description for Check if a resource name is available. |
| <CopyableCode code="move" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Description for Move resources between resource groups. |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, data__location, data__name, data__properties, data__type" /> | Description for Validate if a resource can be created. |
| <CopyableCode code="validate_move" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Description for Validate whether a resource can be moved. |
| <CopyableCode code="verify_hosting_environment_vnet" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Description for Verifies if this VNET is compatible with an App Service Environment by analyzing the Network Security Group rules. |
