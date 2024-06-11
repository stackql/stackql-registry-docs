---
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
  - iam
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

Contains the response to a successful <a>GetPolicy</a> request. 

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Contains the response to a successful <a>GetPolicy</a> request. </td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iam.policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="Policy" /></td><td><code>object</code></td><td>A structure containing details about the policy.</td></tr>
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
    <td><CopyableCode code="get" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="PolicyArn, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="create" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="PolicyDocument, PolicyName, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="PolicyArn, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="tag" /></td>
    <td><code>EXEC</code></td>
    <td><CopyableCode code="PolicyArn, Tags, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="untag" /></td>
    <td><code>EXEC</code></td>
    <td><CopyableCode code="PolicyArn, TagKeys, region" /></td>
  </tr>
</tbody></table>








