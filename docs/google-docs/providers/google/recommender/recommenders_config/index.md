---
title: recommenders_config
hide_title: false
hide_table_of_contents: false
keywords:
  - recommenders_config
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

Creates, updates, deletes, gets or lists a <code>recommenders_config</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>recommenders_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.recommender.recommenders_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Name of recommender config. Eg, projects/[PROJECT_NUMBER]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]/config |
| <CopyableCode code="annotations" /> | `object` | Allows clients to store small amounts of arbitrary data. Annotations must follow the Kubernetes syntax. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between. |
| <CopyableCode code="displayName" /> | `string` | A user-settable field to provide a human-readable name to be used in user interfaces. |
| <CopyableCode code="etag" /> | `string` | Fingerprint of the RecommenderConfig. Provides optimistic locking when updating. |
| <CopyableCode code="recommenderGenerationConfig" /> | `object` | A Configuration to customize the generation of recommendations. Eg, customizing the lookback period considered when generating a recommendation. |
| <CopyableCode code="revisionId" /> | `string` | Output only. Immutable. The revision ID of the config. A new revision is committed whenever the config is changed in any way. The format is an 8-character hexadecimal string. |
| <CopyableCode code="updateTime" /> | `string` | Last time when the config was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="billing_accounts_locations_recommenders_get_config" /> | `SELECT` | <CopyableCode code="billingAccountsId, locationsId, recommendersId" /> | Gets the requested Recommender Config. There is only one instance of the config for each Recommender. |
| <CopyableCode code="organizations_locations_recommenders_get_config" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId, recommendersId" /> | Gets the requested Recommender Config. There is only one instance of the config for each Recommender. |
| <CopyableCode code="projects_locations_recommenders_get_config" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, recommendersId" /> | Gets the requested Recommender Config. There is only one instance of the config for each Recommender. |
| <CopyableCode code="billing_accounts_locations_recommenders_update_config" /> | `UPDATE` | <CopyableCode code="billingAccountsId, locationsId, recommendersId" /> | Updates a Recommender Config. This will create a new revision of the config. |
| <CopyableCode code="organizations_locations_recommenders_update_config" /> | `UPDATE` | <CopyableCode code="locationsId, organizationsId, recommendersId" /> | Updates a Recommender Config. This will create a new revision of the config. |
| <CopyableCode code="projects_locations_recommenders_update_config" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, recommendersId" /> | Updates a Recommender Config. This will create a new revision of the config. |

## `SELECT` examples

Gets the requested Recommender Config. There is only one instance of the config for each Recommender.

```sql
SELECT
name,
annotations,
displayName,
etag,
recommenderGenerationConfig,
revisionId,
updateTime
FROM google.recommender.recommenders_config
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND recommendersId = '{{ recommendersId }}'; 
```

## `UPDATE` example

Updates a <code>recommenders_config</code> resource.

```sql
/*+ update */
UPDATE google.recommender.recommenders_config
SET 
displayName = '{{ displayName }}',
name = '{{ name }}',
etag = '{{ etag }}',
recommenderGenerationConfig = '{{ recommenderGenerationConfig }}',
annotations = '{{ annotations }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND recommendersId = '{{ recommendersId }}';
```
