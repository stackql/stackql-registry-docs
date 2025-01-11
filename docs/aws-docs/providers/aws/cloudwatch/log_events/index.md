---
title: log_events
hide_title: false
hide_table_of_contents: false
keywords:
  - log_events
  - cloudwatch
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Represents a log event.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>log_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a log event.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudwatch.log_events" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="timestamp" /></td><td><code>integer</code></td><td>The time the event occurred, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>.</td></tr>
<tr><td><CopyableCode code="message" /></td><td><code>string</code></td><td>The data contained in the log event.</td></tr>
<tr><td><CopyableCode code="ingestion_time" /></td><td><code>integer</code></td><td>The time the event was ingested, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="GetLogEvents" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__logStreamName, region" /></td>
  </tr>
</tbody></table>






