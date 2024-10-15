---
title: resources
hide_title: false
hide_table_of_contents: false
keywords:
  - resources
  - netapp
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

Creates, updates, deletes, gets or lists a <code>resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.resources" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="check_file_path_availability" /> | `EXEC` | <CopyableCode code="location, subscriptionId, data__name, data__subnetId" /> | Check if a file path is available. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="location, subscriptionId, data__name, data__resourceGroup, data__type" /> | Check if a resource name is available. |
| <CopyableCode code="check_quota_availability" /> | `EXEC` | <CopyableCode code="location, subscriptionId, data__name, data__resourceGroup, data__type" /> | Check if a quota is available. |
| <CopyableCode code="query_network_sibling_set" /> | `EXEC` | <CopyableCode code="location, subscriptionId, data__networkSiblingSetId, data__subnetId" /> | Get details of the specified network sibling set. |
| <CopyableCode code="query_region_info" /> | `EXEC` | <CopyableCode code="location, subscriptionId" /> | Provides storage to network proximity and logical zone mapping information. |
