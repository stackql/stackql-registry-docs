---
title: trigger_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - trigger_runs
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

Creates, updates, deletes, gets or lists a <code>trigger_runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trigger_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_factory.trigger_runs" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="factoryName, resourceGroupName, runId, subscriptionId, triggerName" /> | Cancel a single trigger instance by runId. |
| <CopyableCode code="query_by_factory" /> | `EXEC` | <CopyableCode code="factoryName, resourceGroupName, subscriptionId, data__lastUpdatedAfter, data__lastUpdatedBefore" /> | Query trigger runs. |
| <CopyableCode code="rerun" /> | `EXEC` | <CopyableCode code="factoryName, resourceGroupName, runId, subscriptionId, triggerName" /> | Rerun single trigger instance by runId. |
