---
title: queries
hide_title: false
hide_table_of_contents: false
keywords:
  - queries
  - cost_management
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

Creates, updates, deletes, gets or lists a <code>queries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cost_management.queries" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="usage" /> | `EXEC` | <CopyableCode code="scope, data__dataset, data__timeframe, data__type" /> | Query the usage data for scope defined. |
| <CopyableCode code="usage_by_external_cloud_provider_type" /> | `EXEC` | <CopyableCode code="externalCloudProviderId, externalCloudProviderType, data__dataset, data__timeframe, data__type" /> | Query the usage data for external cloud provider type defined. |
