---
title: insight_types_config
hide_title: false
hide_table_of_contents: false
keywords:
  - insight_types_config
  - recommender
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

Creates, updates, deletes, gets or lists a <code>insight_types_config</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>insight_types_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.recommender.insight_types_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Name of insight type config. Eg, projects/[PROJECT_NUMBER]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]/config |
| <CopyableCode code="annotations" /> | `object` | Allows clients to store small amounts of arbitrary data. Annotations must follow the Kubernetes syntax. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between. |
| <CopyableCode code="displayName" /> | `string` | A user-settable field to provide a human-readable name to be used in user interfaces. |
| <CopyableCode code="etag" /> | `string` | Fingerprint of the InsightTypeConfig. Provides optimistic locking when updating. |
| <CopyableCode code="insightTypeGenerationConfig" /> | `object` | A configuration to customize the generation of insights. Eg, customizing the lookback period considered when generating a insight. |
| <CopyableCode code="revisionId" /> | `string` | Output only. Immutable. The revision ID of the config. A new revision is committed whenever the config is changed in any way. The format is an 8-character hexadecimal string. |
| <CopyableCode code="updateTime" /> | `string` | Last time when the config was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="billing_accounts_locations_insight_types_get_config" /> | `SELECT` | <CopyableCode code="billingAccountsId, insightTypesId, locationsId" /> | Gets the requested InsightTypeConfig. There is only one instance of the config for each InsightType. |
| <CopyableCode code="organizations_locations_insight_types_get_config" /> | `SELECT` | <CopyableCode code="insightTypesId, locationsId, organizationsId" /> | Gets the requested InsightTypeConfig. There is only one instance of the config for each InsightType. |
| <CopyableCode code="projects_locations_insight_types_get_config" /> | `SELECT` | <CopyableCode code="insightTypesId, locationsId, projectsId" /> | Gets the requested InsightTypeConfig. There is only one instance of the config for each InsightType. |
| <CopyableCode code="billing_accounts_locations_insight_types_update_config" /> | `UPDATE` | <CopyableCode code="billingAccountsId, insightTypesId, locationsId" /> | Updates an InsightTypeConfig change. This will create a new revision of the config. |
| <CopyableCode code="organizations_locations_insight_types_update_config" /> | `UPDATE` | <CopyableCode code="insightTypesId, locationsId, organizationsId" /> | Updates an InsightTypeConfig change. This will create a new revision of the config. |
| <CopyableCode code="projects_locations_insight_types_update_config" /> | `UPDATE` | <CopyableCode code="insightTypesId, locationsId, projectsId" /> | Updates an InsightTypeConfig change. This will create a new revision of the config. |

## `SELECT` examples

Gets the requested InsightTypeConfig. There is only one instance of the config for each InsightType.

```sql
SELECT
name,
annotations,
displayName,
etag,
insightTypeGenerationConfig,
revisionId,
updateTime
FROM google.recommender.insight_types_config
WHERE insightTypesId = '{{ insightTypesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `UPDATE` example

Updates a <code>insight_types_config</code> resource.

```sql
/*+ update */
UPDATE google.recommender.insight_types_config
SET 
name = '{{ name }}',
updateTime = '{{ updateTime }}',
annotations = '{{ annotations }}',
etag = '{{ etag }}',
displayName = '{{ displayName }}',
revisionId = '{{ revisionId }}',
insightTypeGenerationConfig = '{{ insightTypeGenerationConfig }}'
WHERE 
insightTypesId = '{{ insightTypesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
