---
title: envgroups_deployed_ingress_config
hide_title: false
hide_table_of_contents: false
keywords:
  - envgroups_deployed_ingress_config
  - apigee
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

Creates, updates, deletes, gets or lists a <code>envgroups_deployed_ingress_config</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>envgroups_deployed_ingress_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.envgroups_deployed_ingress_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the environment group in the following format: `organizations/{org}/envgroups/{envgroup}`. |
| <CopyableCode code="endpointChainingRules" /> | `array` | A list of proxies in each deployment group for proxy chaining calls. |
| <CopyableCode code="hostnames" /> | `array` | Host names for the environment group. |
| <CopyableCode code="location" /> | `string` | When this message appears in the top-level IngressConfig, this field will be populated in lieu of the inlined routing_rules and hostnames fields. Some URL for downloading the full EnvironmentGroupConfig for this group. |
| <CopyableCode code="revisionId" /> | `string` | Revision id that defines the ordering of the EnvironmentGroupConfig resource. The higher the revision, the more recently the configuration was deployed. |
| <CopyableCode code="routingRules" /> | `array` | Ordered list of routing rules defining how traffic to this environment group's hostnames should be routed to different environments. |
| <CopyableCode code="uid" /> | `string` | A unique id for the environment group config that will only change if the environment group is deleted and recreated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_envgroups_get_deployed_ingress_config" /> | `SELECT` | <CopyableCode code="envgroupsId, organizationsId" /> | Gets the deployed ingress configuration for an environment group. |

## `SELECT` examples

Gets the deployed ingress configuration for an environment group.

```sql
SELECT
name,
endpointChainingRules,
hostnames,
location,
revisionId,
routingRules,
uid
FROM google.apigee.envgroups_deployed_ingress_config
WHERE envgroupsId = '{{ envgroupsId }}'
AND organizationsId = '{{ organizationsId }}';
```
