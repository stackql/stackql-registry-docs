---
title: distributions
hide_title: false
hide_table_of_contents: false
keywords:
  - distributions
  - cloudfront
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

Creates, updates, deletes or gets a <code>distribution</code> resource or lists <code>distributions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>distributions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A distribution tells CloudFront where you want content to be delivered from, and the details about how to track and manage content delivery.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudfront.distributions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="distribution_config" /></td><td><code>object</code></td><td>The distribution's configuration.</td></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A complex type that contains zero or more <code>Tag</code> elements.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="DistributionConfig, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>distributions</code> in a region.
```sql
SELECT
region,
id
FROM aws.cloudfront.distributions
;
```
Gets all properties from a <code>distribution</code>.
```sql
SELECT
region,
distribution_config,
domain_name,
id,
tags
FROM aws.cloudfront.distributions
WHERE data__Identifier = '<Id>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>distribution</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.cloudfront.distributions (
 DistributionConfig,
 region
)
SELECT 
'{{ DistributionConfig }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cloudfront.distributions (
 DistributionConfig,
 Tags,
 region
)
SELECT 
 '{{ DistributionConfig }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: distribution
    props:
      - name: DistributionConfig
        value:
          Aliases:
            - '{{ Aliases[0] }}'
          CNAMEs:
            - '{{ CNAMEs[0] }}'
          CacheBehaviors:
            - AllowedMethods:
                - '{{ AllowedMethods[0] }}'
              CachePolicyId: '{{ CachePolicyId }}'
              CachedMethods:
                - '{{ CachedMethods[0] }}'
              Compress: '{{ Compress }}'
              DefaultTTL: null
              FieldLevelEncryptionId: '{{ FieldLevelEncryptionId }}'
              ForwardedValues:
                Cookies:
                  Forward: '{{ Forward }}'
                  WhitelistedNames:
                    - '{{ WhitelistedNames[0] }}'
                Headers:
                  - '{{ Headers[0] }}'
                QueryString: '{{ QueryString }}'
                QueryStringCacheKeys:
                  - '{{ QueryStringCacheKeys[0] }}'
              FunctionAssociations:
                - EventType: '{{ EventType }}'
                  FunctionARN: '{{ FunctionARN }}'
              LambdaFunctionAssociations:
                - EventType: '{{ EventType }}'
                  IncludeBody: '{{ IncludeBody }}'
                  LambdaFunctionARN: '{{ LambdaFunctionARN }}'
              MaxTTL: null
              MinTTL: null
              OriginRequestPolicyId: '{{ OriginRequestPolicyId }}'
              PathPattern: '{{ PathPattern }}'
              RealtimeLogConfigArn: '{{ RealtimeLogConfigArn }}'
              ResponseHeadersPolicyId: '{{ ResponseHeadersPolicyId }}'
              SmoothStreaming: '{{ SmoothStreaming }}'
              TargetOriginId: '{{ TargetOriginId }}'
              TrustedKeyGroups:
                - '{{ TrustedKeyGroups[0] }}'
              TrustedSigners:
                - '{{ TrustedSigners[0] }}'
              ViewerProtocolPolicy: '{{ ViewerProtocolPolicy }}'
          Comment: '{{ Comment }}'
          ContinuousDeploymentPolicyId: '{{ ContinuousDeploymentPolicyId }}'
          CustomErrorResponses:
            - ErrorCachingMinTTL: null
              ErrorCode: '{{ ErrorCode }}'
              ResponseCode: '{{ ResponseCode }}'
              ResponsePagePath: '{{ ResponsePagePath }}'
          CustomOrigin:
            DNSName: '{{ DNSName }}'
            HTTPPort: '{{ HTTPPort }}'
            HTTPSPort: '{{ HTTPSPort }}'
            OriginProtocolPolicy: '{{ OriginProtocolPolicy }}'
            OriginSSLProtocols:
              - '{{ OriginSSLProtocols[0] }}'
          DefaultCacheBehavior:
            AllowedMethods:
              - '{{ AllowedMethods[0] }}'
            CachePolicyId: '{{ CachePolicyId }}'
            CachedMethods:
              - '{{ CachedMethods[0] }}'
            Compress: '{{ Compress }}'
            DefaultTTL: null
            FieldLevelEncryptionId: '{{ FieldLevelEncryptionId }}'
            ForwardedValues: null
            FunctionAssociations:
              - null
            LambdaFunctionAssociations:
              - null
            MaxTTL: null
            MinTTL: null
            OriginRequestPolicyId: '{{ OriginRequestPolicyId }}'
            RealtimeLogConfigArn: '{{ RealtimeLogConfigArn }}'
            ResponseHeadersPolicyId: '{{ ResponseHeadersPolicyId }}'
            SmoothStreaming: '{{ SmoothStreaming }}'
            TargetOriginId: '{{ TargetOriginId }}'
            TrustedKeyGroups:
              - '{{ TrustedKeyGroups[0] }}'
            TrustedSigners:
              - '{{ TrustedSigners[0] }}'
            ViewerProtocolPolicy: '{{ ViewerProtocolPolicy }}'
          DefaultRootObject: '{{ DefaultRootObject }}'
          Enabled: '{{ Enabled }}'
          HttpVersion: '{{ HttpVersion }}'
          IPV6Enabled: '{{ IPV6Enabled }}'
          Logging:
            Bucket: '{{ Bucket }}'
            IncludeCookies: '{{ IncludeCookies }}'
            Prefix: '{{ Prefix }}'
          OriginGroups:
            Items:
              - FailoverCriteria:
                  StatusCodes:
                    Items:
                      - '{{ Items[0] }}'
                    Quantity: '{{ Quantity }}'
                Id: '{{ Id }}'
                Members:
                  Items:
                    - OriginId: '{{ OriginId }}'
                  Quantity: '{{ Quantity }}'
            Quantity: '{{ Quantity }}'
          Origins:
            - ConnectionAttempts: '{{ ConnectionAttempts }}'
              ConnectionTimeout: '{{ ConnectionTimeout }}'
              CustomOriginConfig:
                HTTPPort: '{{ HTTPPort }}'
                HTTPSPort: '{{ HTTPSPort }}'
                OriginKeepaliveTimeout: '{{ OriginKeepaliveTimeout }}'
                OriginProtocolPolicy: '{{ OriginProtocolPolicy }}'
                OriginReadTimeout: '{{ OriginReadTimeout }}'
                OriginSSLProtocols:
                  - '{{ OriginSSLProtocols[0] }}'
              DomainName: '{{ DomainName }}'
              Id: '{{ Id }}'
              OriginAccessControlId: '{{ OriginAccessControlId }}'
              OriginCustomHeaders:
                - HeaderName: '{{ HeaderName }}'
                  HeaderValue: '{{ HeaderValue }}'
              OriginPath: '{{ OriginPath }}'
              OriginShield:
                Enabled: '{{ Enabled }}'
                OriginShieldRegion: '{{ OriginShieldRegion }}'
              S3OriginConfig:
                OriginAccessIdentity: '{{ OriginAccessIdentity }}'
          PriceClass: '{{ PriceClass }}'
          Restrictions:
            GeoRestriction:
              Locations:
                - '{{ Locations[0] }}'
              RestrictionType: '{{ RestrictionType }}'
          S3Origin:
            DNSName: '{{ DNSName }}'
            OriginAccessIdentity: '{{ OriginAccessIdentity }}'
          Staging: '{{ Staging }}'
          ViewerCertificate:
            AcmCertificateArn: '{{ AcmCertificateArn }}'
            CloudFrontDefaultCertificate: '{{ CloudFrontDefaultCertificate }}'
            IamCertificateId: '{{ IamCertificateId }}'
            MinimumProtocolVersion: '{{ MinimumProtocolVersion }}'
            SslSupportMethod: '{{ SslSupportMethod }}'
          WebACLId: '{{ WebACLId }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.cloudfront.distributions
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>distributions</code> resource, the following permissions are required:

### Create
```json
cloudfront:CreateDistribution,
cloudfront:CreateDistributionWithTags,
cloudfront:GetDistribution,
cloudfront:GetDistributionConfig,
cloudfront:TagResource
```

### Delete
```json
cloudfront:DeleteDistribution,
cloudfront:GetDistribution,
cloudfront:GetDistributionConfig
```

### List
```json
cloudfront:ListDistributions
```

### Read
```json
cloudfront:GetDistribution,
cloudfront:GetDistributionConfig
```

### Update
```json
cloudfront:GetDistribution,
cloudfront:GetDistributionConfig,
cloudfront:UpdateDistribution,
cloudfront:UpdateDistributionWithStagingConfig,
cloudfront:ListTagsForResource,
cloudfront:TagResource,
cloudfront:UntagResource
```

