---
title: rule_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - rule_groups
  - wafv2
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


Used to retrieve a list of <code>rule_groups</code> in a region or to create or delete a <code>rule_groups</code> resource, use <code>rule_group</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rule_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Contains the Rules that identify the requests that you want to allow, block, or count. In a RuleGroup, you also specify a default action (ALLOW or BLOCK), and the action for each Rule that you add to a RuleGroup, for example, block requests from specified IP addresses or block requests from specified referrers. You also associate the RuleGroup with a CloudFront distribution to identify the requests that you want AWS WAF to filter. If you add more than one Rule to a RuleGroup, a request needs to match only one of the specifications to be allowed, blocked, or counted.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.wafv2.rule_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="scope" /></td><td><code>undefined</code></td><td></td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
name,
id,
scope
FROM aws.wafv2.rule_groups
;
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "Capacity": "{{ Capacity }}",
 "Scope": "{{ Scope }}",
 "VisibilityConfig": {
  "SampledRequestsEnabled": "{{ SampledRequestsEnabled }}",
  "CloudWatchMetricsEnabled": "{{ CloudWatchMetricsEnabled }}",
  "MetricName": "{{ MetricName }}"
 }
}
>>>
--required properties only
INSERT INTO aws.wafv2.rule_groups (
 Capacity,
 Scope,
 VisibilityConfig,
 region
)
SELECT 
{{ .Capacity }},
 {{ .Scope }},
 {{ .VisibilityConfig }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Capacity": "{{ Capacity }}",
 "Description": "{{ Description }}",
 "Name": "{{ Name }}",
 "Scope": "{{ Scope }}",
 "Rules": [
  {
   "Name": null,
   "Priority": "{{ Priority }}",
   "Statement": {
    "ByteMatchStatement": {
     "SearchString": "{{ SearchString }}",
     "SearchStringBase64": "{{ SearchStringBase64 }}",
     "FieldToMatch": {
      "SingleHeader": {
       "Name": "{{ Name }}"
      },
      "SingleQueryArgument": {
       "Name": "{{ Name }}"
      },
      "AllQueryArguments": {},
      "UriPath": {},
      "QueryString": {},
      "Body": {
       "OversizeHandling": "{{ OversizeHandling }}"
      },
      "Method": {},
      "JsonBody": {
       "MatchPattern": {
        "All": {},
        "IncludedPaths": [
         "{{ IncludedPaths[0] }}"
        ]
       },
       "MatchScope": "{{ MatchScope }}",
       "InvalidFallbackBehavior": "{{ InvalidFallbackBehavior }}",
       "OversizeHandling": null
      },
      "Headers": {
       "MatchPattern": {
        "All": {},
        "IncludedHeaders": [
         "{{ IncludedHeaders[0] }}"
        ],
        "ExcludedHeaders": [
         "{{ ExcludedHeaders[0] }}"
        ]
       },
       "MatchScope": "{{ MatchScope }}",
       "OversizeHandling": null
      },
      "Cookies": {
       "MatchPattern": {
        "All": {},
        "IncludedCookies": [
         "{{ IncludedCookies[0] }}"
        ],
        "ExcludedCookies": [
         "{{ ExcludedCookies[0] }}"
        ]
       },
       "MatchScope": null,
       "OversizeHandling": null
      },
      "JA3Fingerprint": {
       "FallbackBehavior": "{{ FallbackBehavior }}"
      }
     },
     "TextTransformations": [
      {
       "Priority": "{{ Priority }}",
       "Type": "{{ Type }}"
      }
     ],
     "PositionalConstraint": "{{ PositionalConstraint }}"
    },
    "SqliMatchStatement": {
     "FieldToMatch": null,
     "TextTransformations": [
      null
     ],
     "SensitivityLevel": "{{ SensitivityLevel }}"
    },
    "XssMatchStatement": {
     "FieldToMatch": null,
     "TextTransformations": [
      null
     ]
    },
    "SizeConstraintStatement": {
     "FieldToMatch": null,
     "ComparisonOperator": "{{ ComparisonOperator }}",
     "Size": null,
     "TextTransformations": [
      null
     ]
    },
    "GeoMatchStatement": {
     "CountryCodes": [
      "{{ CountryCodes[0] }}"
     ],
     "ForwardedIPConfig": {
      "HeaderName": "{{ HeaderName }}",
      "FallbackBehavior": "{{ FallbackBehavior }}"
     }
    },
    "RuleGroupReferenceStatement": {
     "Arn": "{{ Arn }}",
     "ExcludedRules": [
      {
       "Name": null
      }
     ],
     "RuleActionOverrides": [
      {
       "Name": null,
       "ActionToUse": {
        "Allow": {
         "CustomRequestHandling": {
          "InsertHeaders": [
           {
            "Name": "{{ Name }}",
            "Value": "{{ Value }}"
           }
          ]
         }
        },
        "Block": {
         "CustomResponse": {
          "ResponseCode": "{{ ResponseCode }}",
          "CustomResponseBodyKey": "{{ CustomResponseBodyKey }}",
          "ResponseHeaders": [
           null
          ]
         }
        },
        "Count": {
         "CustomRequestHandling": null
        },
        "Captcha": {
         "CustomRequestHandling": null
        },
        "Challenge": {
         "CustomRequestHandling": null
        }
       }
      }
     ]
    },
    "IPSetReferenceStatement": {
     "Arn": null,
     "IPSetForwardedIPConfig": {
      "HeaderName": "{{ HeaderName }}",
      "FallbackBehavior": "{{ FallbackBehavior }}",
      "Position": "{{ Position }}"
     }
    },
    "RegexPatternSetReferenceStatement": {
     "Arn": null,
     "FieldToMatch": null,
     "TextTransformations": [
      null
     ]
    },
    "ManagedRuleGroupStatement": {
     "Name": null,
     "VendorName": "{{ VendorName }}",
     "Version": "{{ Version }}",
     "ExcludedRules": [
      null
     ],
     "ScopeDownStatement": null,
     "ManagedRuleGroupConfigs": [
      {
       "LoginPath": "{{ LoginPath }}",
       "PayloadType": "{{ PayloadType }}",
       "UsernameField": {
        "Identifier": "{{ Identifier }}"
       },
       "PasswordField": null,
       "AWSManagedRulesBotControlRuleSet": {
        "InspectionLevel": "{{ InspectionLevel }}",
        "EnableMachineLearning": "{{ EnableMachineLearning }}"
       },
       "AWSManagedRulesATPRuleSet": {
        "LoginPath": "{{ LoginPath }}",
        "EnableRegexInPath": "{{ EnableRegexInPath }}",
        "RequestInspection": {
         "PayloadType": "{{ PayloadType }}",
         "UsernameField": null,
         "PasswordField": null
        },
        "ResponseInspection": {
         "StatusCode": {
          "SuccessCodes": [
           "{{ SuccessCodes[0] }}"
          ],
          "FailureCodes": [
           "{{ FailureCodes[0] }}"
          ]
         },
         "Header": {
          "Name": "{{ Name }}",
          "SuccessValues": [
           "{{ SuccessValues[0] }}"
          ],
          "FailureValues": [
           "{{ FailureValues[0] }}"
          ]
         },
         "BodyContains": {
          "SuccessStrings": [
           "{{ SuccessStrings[0] }}"
          ],
          "FailureStrings": [
           "{{ FailureStrings[0] }}"
          ]
         },
         "Json": {
          "Identifier": "{{ Identifier }}",
          "SuccessValues": [
           "{{ SuccessValues[0] }}"
          ],
          "FailureValues": [
           "{{ FailureValues[0] }}"
          ]
         }
        }
       },
       "AWSManagedRulesACFPRuleSet": {
        "CreationPath": "{{ CreationPath }}",
        "RegistrationPagePath": "{{ RegistrationPagePath }}",
        "RequestInspection": {
         "PayloadType": "{{ PayloadType }}",
         "UsernameField": null,
         "PasswordField": null,
         "EmailField": null,
         "PhoneNumberFields": [
          null
         ],
         "AddressFields": [
          null
         ]
        },
        "ResponseInspection": null,
        "EnableRegexInPath": "{{ EnableRegexInPath }}"
       }
      }
     ],
     "RuleActionOverrides": [
      null
     ]
    },
    "RateBasedStatement": {
     "Limit": "{{ Limit }}",
     "EvaluationWindowSec": "{{ EvaluationWindowSec }}",
     "AggregateKeyType": "{{ AggregateKeyType }}",
     "CustomKeys": [
      {
       "Cookie": {
        "Name": "{{ Name }}",
        "TextTransformations": [
         null
        ]
       },
       "ForwardedIP": {},
       "Header": {
        "Name": "{{ Name }}",
        "TextTransformations": [
         null
        ]
       },
       "HTTPMethod": {},
       "IP": {},
       "LabelNamespace": {
        "Namespace": "{{ Namespace }}"
       },
       "QueryArgument": {
        "Name": "{{ Name }}",
        "TextTransformations": [
         null
        ]
       },
       "QueryString": {
        "TextTransformations": [
         null
        ]
       },
       "UriPath": {
        "TextTransformations": [
         null
        ]
       }
      }
     ],
     "ScopeDownStatement": null,
     "ForwardedIPConfig": null
    },
    "AndStatement": {
     "Statements": [
      null
     ]
    },
    "OrStatement": {
     "Statements": [
      null
     ]
    },
    "NotStatement": {
     "Statement": null
    },
    "LabelMatchStatement": {
     "Scope": "{{ Scope }}",
     "Key": "{{ Key }}"
    },
    "RegexMatchStatement": {
     "RegexString": "{{ RegexString }}",
     "FieldToMatch": null,
     "TextTransformations": [
      null
     ]
    }
   },
   "Action": null,
   "OverrideAction": {
    "Count": {},
    "None": {}
   },
   "RuleLabels": [
    {
     "Name": "{{ Name }}"
    }
   ],
   "VisibilityConfig": {
    "SampledRequestsEnabled": "{{ SampledRequestsEnabled }}",
    "CloudWatchMetricsEnabled": "{{ CloudWatchMetricsEnabled }}",
    "MetricName": "{{ MetricName }}"
   },
   "CaptchaConfig": {
    "ImmunityTimeProperty": {
     "ImmunityTime": "{{ ImmunityTime }}"
    }
   },
   "ChallengeConfig": {
    "ImmunityTimeProperty": null
   }
  }
 ],
 "VisibilityConfig": null,
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "CustomResponseBodies": {},
 "AvailableLabels": [
  {
   "Name": null
  }
 ],
 "ConsumedLabels": [
  null
 ]
}
>>>
--all properties
INSERT INTO aws.wafv2.rule_groups (
 Capacity,
 Description,
 Name,
 Scope,
 Rules,
 VisibilityConfig,
 Tags,
 CustomResponseBodies,
 AvailableLabels,
 ConsumedLabels,
 region
)
SELECT 
 {{ .Capacity }},
 {{ .Description }},
 {{ .Name }},
 {{ .Scope }},
 {{ .Rules }},
 {{ .VisibilityConfig }},
 {{ .Tags }},
 {{ .CustomResponseBodies }},
 {{ .AvailableLabels }},
 {{ .ConsumedLabels }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.wafv2.rule_groups
WHERE data__Identifier = '<Name|Id|Scope>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>rule_groups</code> resource, the following permissions are required:

### Create
```json
wafv2:CreateRuleGroup,
wafv2:GetRuleGroup,
wafv2:ListTagsForResource
```

### Delete
```json
wafv2:DeleteRuleGroup,
wafv2:GetRuleGroup
```

### List
```json
wafv2:listRuleGroups
```

