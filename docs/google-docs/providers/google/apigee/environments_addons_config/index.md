---
title: environments_addons_config
hide_title: false
hide_table_of_contents: false
keywords:
  - environments_addons_config
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments_addons_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.environments_addons_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="advancedApiOpsConfig" /> | `object` | Configuration for the Advanced API Ops add-on. |
| <CopyableCode code="analyticsConfig" /> | `object` | Configuration for the Analytics add-on. |
| <CopyableCode code="apiSecurityConfig" /> | `object` | Configurations of the API Security add-on. |
| <CopyableCode code="connectorsPlatformConfig" /> | `object` | Configuration for the Connectors Platform add-on. |
| <CopyableCode code="integrationConfig" /> | `object` | Configuration for the Integration add-on. |
| <CopyableCode code="monetizationConfig" /> | `object` | Configuration for the Monetization add-on. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="organizations_environments_get_addons_config" /> | `SELECT` | <CopyableCode code="environmentsId, organizationsId" /> |
