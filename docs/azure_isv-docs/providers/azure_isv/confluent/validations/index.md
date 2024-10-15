---
title: validations
hide_title: false
hide_table_of_contents: false
keywords:
  - validations
  - confluent
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

Creates, updates, deletes, gets or lists a <code>validations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>validations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.confluent.validations" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="validate_organization" /> | `EXEC` | <CopyableCode code="organizationName, resourceGroupName, subscriptionId, data__properties" /> |  |
| <CopyableCode code="validate_organization_v2" /> | `EXEC` | <CopyableCode code="organizationName, resourceGroupName, subscriptionId, data__properties" /> |  |
