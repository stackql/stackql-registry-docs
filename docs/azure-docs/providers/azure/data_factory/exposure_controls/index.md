---
title: exposure_controls
hide_title: false
hide_table_of_contents: false
keywords:
  - exposure_controls
  - data_factory
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

Creates, updates, deletes, gets or lists a <code>exposure_controls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>exposure_controls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_factory.exposure_controls" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="query_feature_values_by_factory" /> | `EXEC` | <CopyableCode code="factoryName, resourceGroupName, subscriptionId, data__exposureControlRequests" /> | Get list of exposure control features for specific factory. |
