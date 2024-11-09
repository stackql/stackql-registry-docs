---
title: compatibilities
hide_title: false
hide_table_of_contents: false
keywords:
  - compatibilities
  - schema_registry
  - azure
  - microsoft azure
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Microsoft Azure infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>compatibilities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>compatibilities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.schema_registry.compatibilities" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="test_compatibility_by_subject_name" /> | `EXEC` | <CopyableCode code="subject, version" /> | Test input schema against a particular version of a subject's schema for compatibility. The compatibility level applied for the check is the configured compatibility level for the subject (http:get:: /config/(string: subject)). If this subject's compatibility level was never changed, then the global compatibility level applies (http:get:: /config). |
| <CopyableCode code="test_compatibility_for_subject" /> | `EXEC` | <CopyableCode code="subject" /> | Test input schema against a subject's schemas for compatibility, based on the configured compatibility level of the subject. In other words, it will perform the same compatibility check as register for that subject. The compatibility level applied for the check is the configured compatibility level for the subject (http:get:: /config/(string: subject)). If this subject's compatibility level was never changed, then the global compatibility level applies (http:get:: /config). |
