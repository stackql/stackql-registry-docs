---
title: rollouts
hide_title: false
hide_table_of_contents: false
keywords:
  - rollouts
  - servicemanagement
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rollouts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.servicemanagement.rollouts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="createTime" /> | `string` | Creation time of the rollout. Readonly. |
| <CopyableCode code="createdBy" /> | `string` | The user who created the Rollout. Readonly. |
| <CopyableCode code="deleteServiceStrategy" /> | `object` | Strategy used to delete a service. This strategy is a placeholder only used by the system generated rollout to delete a service. |
| <CopyableCode code="rolloutId" /> | `string` | Optional. Unique identifier of this Rollout. Must be no longer than 63 characters and only lower case letters, digits, '.', '_' and '-' are allowed. If not specified by client, the server will generate one. The generated id will have the form of , where "date" is the create date in ISO 8601 format. "revision number" is a monotonically increasing positive number that is reset every day for each service. An example of the generated rollout_id is '2016-02-16r1' |
| <CopyableCode code="serviceName" /> | `string` | The name of the service associated with this Rollout. |
| <CopyableCode code="status" /> | `string` | The status of this rollout. Readonly. In case of a failed rollout, the system will automatically rollback to the current Rollout version. Readonly. |
| <CopyableCode code="trafficPercentStrategy" /> | `object` | Strategy that specifies how clients of Google Service Controller want to send traffic to use different config versions. This is generally used by API proxy to split traffic based on your configured percentage for each config version. One example of how to gradually rollout a new service configuration using this strategy: Day 1 Rollout &#123; id: "example.googleapis.com/rollout_20160206" traffic_percent_strategy &#123; percentages: &#123; "example.googleapis.com/20160201": 70.00 "example.googleapis.com/20160206": 30.00 &#125; &#125; &#125; Day 2 Rollout &#123; id: "example.googleapis.com/rollout_20160207" traffic_percent_strategy: &#123; percentages: &#123; "example.googleapis.com/20160206": 100.00 &#125; &#125; &#125; |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="rolloutId, serviceName" /> | Gets a service configuration rollout. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="serviceName" /> | Lists the history of the service configuration rollouts for a managed service, from the newest to the oldest. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="serviceName" /> | Creates a new service configuration rollout. Based on rollout, the Google Service Management will roll out the service configurations to different backend services. For example, the logging configuration will be pushed to Google Cloud Logging. Please note that any previous pending and running Rollouts and associated Operations will be automatically cancelled so that the latest Rollout will not be blocked by previous Rollouts. Only the 100 most recent (in any state) and the last 10 successful (if not already part of the set of 100 most recent) rollouts are kept for each service. The rest will be deleted eventually. Operation |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="serviceName" /> | Lists the history of the service configuration rollouts for a managed service, from the newest to the oldest. |
