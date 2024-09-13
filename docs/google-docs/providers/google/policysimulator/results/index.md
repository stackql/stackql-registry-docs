---
title: results
hide_title: false
hide_table_of_contents: false
keywords:
  - results
  - policysimulator
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

Creates, updates, deletes, gets or lists a <code>results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.policysimulator.results" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the `ReplayResult`, in the following format: `{projects|folders|organizations}/{resource-id}/locations/global/replays/{replay-id}/results/{replay-result-id}`, where `{resource-id}` is the ID of the project, folder, or organization that owns the Replay. Example: `projects/my-example-project/locations/global/replays/506a5f7f-38ce-4d7d-8e03-479ce1833c36/results/1234` |
| <CopyableCode code="accessTuple" /> | `object` | Information about the principal, resource, and permission to check. |
| <CopyableCode code="diff" /> | `object` | The difference between the results of evaluating an access tuple under the current (baseline) policies and under the proposed (simulated) policies. This difference explains how a principal's access could change if the proposed policies were applied. |
| <CopyableCode code="error" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="lastSeenDate" /> | `object` | Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following: * A full date, with non-zero year, month, and day values. * A month and day, with a zero year (for example, an anniversary). * A year on its own, with a zero month and a zero day. * A year and month, with a zero day (for example, a credit card expiration date). Related types: * google.type.TimeOfDay * google.type.DateTime * google.protobuf.Timestamp |
| <CopyableCode code="parent" /> | `string` | The Replay that the access tuple was included in. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="folders_locations_replays_results_list" /> | `SELECT` | <CopyableCode code="foldersId, locationsId, replaysId" /> | Lists the results of running a Replay. |
| <CopyableCode code="organizations_locations_replays_results_list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId, replaysId" /> | Lists the results of running a Replay. |
| <CopyableCode code="projects_locations_replays_results_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, replaysId" /> | Lists the results of running a Replay. |

## `SELECT` examples

Lists the results of running a Replay.

```sql
SELECT
name,
accessTuple,
diff,
error,
lastSeenDate,
parent
FROM google.policysimulator.results
WHERE foldersId = '{{ foldersId }}'
AND locationsId = '{{ locationsId }}'
AND replaysId = '{{ replaysId }}'; 
```
