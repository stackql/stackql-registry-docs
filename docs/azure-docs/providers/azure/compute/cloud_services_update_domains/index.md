---
title: cloud_services_update_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_services_update_domains
  - compute
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

Creates, updates, deletes, gets or lists a <code>cloud_services_update_domains</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_services_update_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.cloud_services_update_domains" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="walk_update_domain" /> | `EXEC` | <CopyableCode code="cloudServiceName, resourceGroupName, subscriptionId, updateDomain" /> | Updates the role instances in the specified update domain. |
