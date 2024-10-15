---
title: activity_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - activity_runs
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

Creates, updates, deletes, gets or lists a <code>activity_runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>activity_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_factory.activity_runs" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="query_by_pipeline_run" /> | `EXEC` | <CopyableCode code="factoryName, resourceGroupName, runId, subscriptionId, data__lastUpdatedAfter, data__lastUpdatedBefore" /> | Query activity runs based on input filter conditions. |
